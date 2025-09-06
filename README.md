
ProTraderHack Firebase package (admin panel + rules)

Files:
- admin_index.html  --> Static admin UI. Paste your Firebase config then sign in with admin account.
- firestore.rules    --> Firestore security rules file. Paste into Firebase Rules tab.
- README.md          --> this file.

How to use:
1. In Firebase Console -> Firestore -> Rules: replace with content of firestore.rules and publish.
2. In Firebase Console -> Storage: ensure rules allow read for authenticated users (default is ok).
3. Create 'users' document for your admin UID with field role='admin' (in Firestore Data).
4. Open admin_index.html in browser (or host via Firebase Hosting) and paste your Firebase web config (from Project Settings -> SDK).
5. Sign in with admin email/password (admin must exist in Authentication users).
6. Use the admin UI to post signals and proofs.
7. Frontend apps should add Firestore listeners to /signals to display charts and proofs in real-time.
