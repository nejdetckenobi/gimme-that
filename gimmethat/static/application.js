app = new Vue({
    'el': '#app',
    'data': {
        'file_list': [],
        'percentage': 0.0,
        'abort': false
    },
    'methods': {
        get_file_list() {
            this.file_list = document.getElementById('file-input').files;
        },
        send_files() {
            if(this.file_list.length === 0) {
                return;
            }
            let fd = new FormData();
            for (var i = 0; i < this.file_list.length; i++) {
                fd.append(this.file_list[i].name, this.file_list[i]);
            }
            let xhr = new XMLHttpRequest();
            xhr.open('POST', '/upload', true);
            application = this;
            xhr.upload.onprogress = function (e) {
                if (e.lengthComputable) {
                    application.percentage = (e.loaded / e.total) * 100;
                }
                if (application.abort) {
                    xhr.abort();
                    xhr.percentage = 0;
                }
            };
            xhr.onload = function (e) {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        // window.location = '/success';
                    } else if (xhr.status == 413) {
                        console.error(xhr.statusText);
                        alert('Total file size is too large.');
                        app.percentage = 0;
                    } else {
                        console.error(xhr.statusText);
                        alert(xhr.statusText);
                        app.percentage = 0;
                    }
                }
            };
            xhr.onerror = function (e) {
                alert("Connection problems.");
                app.percentage = 0;
            }
            xhr.send(fd);
        }
    }
});
