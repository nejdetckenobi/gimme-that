app = new Vue({
    'el': '#app',
    'data': {
        'file_list': [],
        'percentage': 0.0,
        'abort': false,
        'is_drag_active': false
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
            xhr.open('POST', '/', true);
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
        },
        ondragover_handler(e) {
        },
        ondrop_handler(e) {
            this.is_drag_active = false;
            this.file_list = [];
            document.getElementById('file-input').files = e.dataTransfer.files;
        },
        ondragend_handler(e) {
            this.is_drag_active = false;
        },
        ondragleave_handler(e) {
            this.is_drag_active = false;
        },
        ondragenter_handler(e) {
            this.is_drag_active = true;
        },
        ondragexit_handler(e) {
            this.is_drag_active = false;
        }
    }
});
