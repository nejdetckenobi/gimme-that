install:
	@echo "Getting Bootstrap 3.3.7"
	@wget "https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip" -O "app/static/bootstrap-3.3.7-dist.zip"
	-@unzip -o "app/static/bootstrap-3.3.7-dist.zip" -d "app/static"
	-@rm -rf "app/static/bootstrap-3.3.7-dist.zip"
	@echo "Getting Vue.js"
	@wget "https://vuejs.org/js/vue.js" -O "app/static/vue.js"
	@echo "Installing dependencies"
	pip install -r "requirements.txt"

run:
	@python run.py

clean:
	@echo "Removing Bootstrap files and folders"
	-@rm -rf "app/static/bootstrap-3.3.7-dist"
	@echo "Removing Vue.js"
	-@rm -f "app/static/vue.js"
