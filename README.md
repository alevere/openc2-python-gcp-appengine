# openc2-python-gcp-appengine

1. Create a new project in Google Cloud Platform
2. Register an SSH key with GCP Cloud Source Repositories
3. Clone this repo to your local computer: 
   a. mkdir appengine
   b. git git clone https://github.com/alevere/openc2-python-gcp-appengine.git
   c. cd openc2-python-gcp-appengine
4. Push into Cloud Source Repositories
   a. git remote add google ssh://{googleuser@domain.com}@source.developers.google.com:2022/p/{project-id}/r/{repo-name}
5. Refresh the Cloud Source Repositories to see your files
6. Prepare Cloud Build, starting with enabling APIs for appengine and cloudbuild for your project
   a. Review https://cloud.google.com/source-repositories/docs/quickstart-triggering-builds-with-source-repositories#grant-app-engine_access-to-cloud_build
7. Enable APIs for your project per https://console.cloud.google.com/flows/enableapi?apiid=appengine.googleapis.com,cloudbuild.googleapis.com&_ga=2.45333668.1893174837.1624365183-1882903627.1623695384
8. Navigate to Cloud Build, then Settings and enable App Engine Admin
9. Navigate to App Engine
10. Click to Create App and select an appropriate region
11. Open Cloud Build Triggers
12. 
