# CARE Frontend

**Parent:** Open HealthCare Network — Project Ideas
**Source:** https://github.com/ohcnetwork/care_fe
**Scraped:** 2026-02-22T23:28:47.599624

---

**Our goal is to continuously improve the quality and accessibility of public healthcare services using digital tools.**

Auto deployed to [care.ohc.network](https://care.ohc.network/) for `develop`

branch. All pull requests have preview builds powered by [Netlify](https://netlify.com).

- 💬 Comment on the issue if you are willing to take it up, and link the pull request with the issue.
- 🏷️ Tag
`@ohcnetwork/care-fe-code-reviewers`

for faster resolution. - 📸 Attach screenshots in the pull requests showing the changes made in the UI.

`npm install`

`npm run dev`

Once the development server has started, open [localhost:4000](http://localhost:4000) in your browser. The page will be automatically reloaded when you make edits and save. You will also see any lint errors in the console.

First, set up the CARE local backend by following the instructions in the [CARE Backend Documentation](https://care-be-docs.ohc.network/).

Create a `.env.local`

file in the root directory of the project :

```
# Point the frontend to your local backend
REACT_CARE_API_URL=http://127.0.0.1:9000
```

Once you have the local backend running and loaded dummy data, you can use the following credentials to authenticate:

```
# Default Local Backend Credentials
ROLE USERNAME PASSWORD
----------------------------------------------------------------
Volunteer volunteer_2_0 Coronasafe@123
Doctor doctor_2_0 Coronasafe@123
Staff staff_2_0 Coronasafe@123
Nurse nurse_2_0 Coronasafe@123
Administrator administrator_2_0 Coronasafe@123
Facility Admin facility_admin_2_0 Coronasafe@123
```

When developing or testing against multiple backend environments (local, staging, production), you can configure the frontend to automatically connect to different backends based on which URL you access it from.

**Configure API URL Mapping in .env.local:**

```
# Map different frontend origins to different backend URLs
REACT_CARE_URL_MAP='{"http://localhost:4000": "https://careapi.ohc.network", "http://care.localhost": "https://careapi.ohc.network", "http://develop.localhost": "https://develop-api.ohc.network", "http://dev.localhost": "http://localhost:9000"}'
# Fallback for any unmatched origins
REACT_CARE_API_URL=https://careapi.ohc.network
```

**Set up Nginx reverse proxy:**

We'll use [Homebrew](https://brew.sh/) to fetch most of the packages on macOS:

- nginx -
`brew install nginx`

. Start Nginx server after installation.

**Important**: Make sure that you start Nginx after you install them. Instructions on how to do that will
be printed to the command-line after it's successfully installed.

The following command should install the required dependencies on Ubuntu. If you're using another *flavour* of Linux, adapt the command to work with the package manager available with your distribution.

```
sudo apt-get install nginx
```


-
Create a new Nginx server configuration file...

`/opt/homebrew/etc/nginx/servers/care`

(macOS)`/etc/nginx/sites-enabled/care`

(Linux)

...and save the following configuration inside it:

`server { listen 80; server_name care.localhost develop.localhost dev.localhost plugs.localhost; location / { proxy_pass http://localhost:4000/; proxy_set_header Host $host; } }`

-
Restart

`nginx`

so that it picks up the new configuration.`# macOS brew services restart nginx # Ubuntu sudo service nginx restart`

On Debian/Ubuntu, NGINX comes with a

`sites-enabled/default`

file which may need to be removed before the Care will begin responding to requests.

If your Nginx reverse-proxy has been set up correctly, then visit the school using your browser at
`http://care.localhost`

.

For patient login via phone number:

- In production, an actual SMS with OTP is sent to the provided phone number
- In staging environment, to save costs, SMS messages are not actually sent
- For testing purposes in staging, use the hardcoded OTP:
`45612`


- Create a branch with branch name of the format
`issues/{issue#}/{short-name}`

(example`issues/7001/edit-prescriptions`

) from the latestbranch when starting to work on an issue.`develop`

- Once the changes are pushed to the branch, make a pull request with a meaningful title (example: "💊 Adds support for editing prescriptions" #6369)
- Ensure the issue number is mentioned in the PR with a closing tag by following the PR body template. (Refer:
[Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)) - Once the code review is done, the PR will be marked with a "Needs Testing" label where it'll be queued for QA testing.
- Once tested, the PR would be marked with a "Tested" label and would be queued for merge.

All strings must be encased in i18n translations. New translation strings must be specified in `src`

->`Locale`

->`en`

. Do not add translations for languages other than english through pull requests. Other language translations can be contributed through [Crowdin](https://crowdin.com/project/ohccarefe)

CARE can load translation files from a remote URL and fall back to local files for any missing keys.

**Enable remote translations**: set`REACT_CUSTOM_REMOTE_I18N_URL`

in your environment.**Expected remote file path**:`${REACT_CUSTOM_REMOTE_I18N_URL}/{lang}.json`

(for example:`https://cdn.example.com/i18n/en.json`

).**Local fallback path**:`/public/locale/{lang}.json`

in this repository (served as`/locale/{lang}.json`

).**Merge behavior**: remote keys override local; any keys absent in remote are served from local.

Example `.env.local`

:

```
# Load i18n from a CDN (per-language JSON files)
REACT_CUSTOM_REMOTE_I18N_URL=https://cdn.example.com/i18n
```

Remote file example (`en.json`

):

```
{
"hello_care": "Hello Care Remote"
}
```

Local file example (`public/locale/en.json`

):

```
{
"hello_care": "Hello Care Local",
"welcome_message": "Welcome to Care"
}
```

With the above, the app serves:

`hello_care`

-> "Hello Care Remote" (remote overrides local)`welcome_message`

-> "Welcome to Care" (falls back to local as remote is missing)

To ensure the quality of our pull requests, we use a variety of tools:

**Automated E2E Testing:**We use Playwright for end-to-end testing to automatically verify the functionality and performance of our code.**Manual Real Device Testing:**We use BrowserStack to manually test our code on real devices, ensuring compatibility and functionality across different platforms and browsers.

To run Playwright tests locally, you'll need to setup the backend to run locally and load dummy data required for the tests. See [docs](https://github.com/ohcnetwork/care#self-hosting).

Once backend is running locally, ensure your local front-end is connected to local backend by setting the `REACT_CARE_API_URL`

environment variable:

```
#.env
REACT_CARE_API_URL=http://127.0.0.1:9000
```

First, install Playwright browsers:

`npm run playwright:install`

Then run Playwright tests in one of the following modes:

```
npm run playwright:test # Run all tests in headless mode
npm run playwright:test:ui # Run tests in interactive UI mode
npm run playwright:test:headed # Run tests in headed mode (visible browser)
npm run playwright:show-report # View the HTML test report
```

- Test results and artifacts are saved in
`test-results/`

- HTML reports are saved in
`playwright-report/`


For more details, see [tests/README.md](https://github.com/ohcnetwork/care_fe/blob/develop/tests/README.md).

`npm run build`

Builds the app for production to the `build`

folder. It correctly bundles React in production mode and optimizes the build for the best performance.

`npm run preview`

Starts a production http-server in local to run the project with Service worker. The build is minified and the filenames include the hashes.

**🚀 Your app is ready to be deployed!**
