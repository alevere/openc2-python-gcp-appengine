# openc2-python-gcp-appengine

1. Create a new project in Google Cloud Platform
2. Prepare Cloud Build, starting with enabling APIs for appengine and cloudbuild for your project a. Review https://cloud.google.com/source-repositories/docs/quickstart-triggering-builds-with-source-repositories#grant-app-engine_access-to-cloud_build
3. Enable APIs for your project per https://console.cloud.google.com/flows/enableapi?apiid=appengine.googleapis.com,cloudbuild.googleapis.com&_ga=2.45333668.1893174837.1624365183-1882903627.1623695384
4. Navigate to App Engine
5. Click to Create App and select an appropriate region
6. If prompted select python and flexible as the AppEngine type
7. Open cloud shell and run
8. wget https://github.com/alevere/openc2-python-gcp-appengine/archive/refs/heads/main.zip
9. unzip main.zip
10. cd openc2-python-gcp-appengine
11. Run 'gcloud app deploy app.yaml'
12. Select 'Y' to continue and eventually this message will appear in the console: 
