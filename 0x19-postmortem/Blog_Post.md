# Postmortem

![Post-mortem meeting](https://i.redd.it/e1fvfqdxncr61.png)

## Issue Summary

After rolling out a new feature to our recently launched Node.js platform, we encountered our first major issue with users reporting problems. Five minutes after the deployment, we started receiving a surge of emails from users saying, "they can't log in or create accounts on the platform." This was unexpected because everything worked fine in our development environment and during previous tests. In total, 150 emails flooded our support inbox, making it clear that the issue was widespread. Given how crucial early users are to a platform, we immediately began investigating. After pulling down the repository from GitHub and following the documented setup steps, we were unable to start the site locally. The root cause became evident: a missing update in one of the project's dependencies. The site remained down from 9:45 AM GMT+1 to 11:10 AM GMT+1.

## Timeline

+08-10-2024 9:45 AM GMT+1 - First user complaint arrives, reporting login and registration issues.
+08-10-2024 10:05 AM GMT+1 - Aria, one of our backend engineers, reproduces the same error locally.
+08-10-2024 10:20 AM GMT+1 - Initial checks focused on API routes and authentication flow.
+08-10-2024 10:30 AM GMT+1 - We hypothesized that a misconfiguration in the OAuth provider's setup could be the issue, but it was ruled out.
+08-10-2024 10:35 AM GMT+1 - Focus shifted to session handling middleware after noticing token generation issues in the error logs.
+08-10-2024 10:45 AM GMT+1 - The team narrowed down the issue to an outdated version of the jsonwebtoken package, which failed to validate user tokens correctly.
+08-10-2024 11:00 AM GMT+1 - The issue was escalated to the full backend team.
+08-10-2024 11:10 AM GMT+1 - The problem was resolved by upgrading the jsonwebtoken package version and redeploying the platform.

## Root Cause And Resolution

The issue stemmed from an outdated version of the jsonwebtoken package used to handle token authentication. The old version was unable to validate tokens correctly, leading to login and signup failures. Aria resolved the issue by updating the jsonwebtoken package to the latest stable version in the package.json file and reinstalling the dependencies. The site functioned properly after the update, and users were able to log in and register without further issues.

## Corrective And Preventative Measures

* Implement automated dependency checking tools to alert us when core packages are outdated.
* Improve test coverage specifically around critical flows like login and registration, ensuring they are part of our continuous integration pipeline.
* Set up real-time monitoring for login and signup success rates, with immediate alerts for any significant drop in performance.