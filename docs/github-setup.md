# Put This Project on GitHub

The project folder is ready to publish as a new GitHub repository. Suggested repository name: `nursery-rhyme-video-director`.

## GitHub website

1. Create an empty repository at [github.com/new](https://github.com/new).
2. Use `nursery-rhyme-video-director` as the repository name.
3. Choose public or private according to your preference.
4. Leave “Add a README,” “Add .gitignore,” and “Choose a license” unchecked because this folder already contains those files.
5. From a terminal in this project folder, run:

   ```bash
   git init -b main
   git add .
   git commit -m "Create nursery rhyme video director kit"
   git remote add origin https://github.com/YOUR-USERNAME/nursery-rhyme-video-director.git
   git push -u origin main
   ```

Replace `YOUR-USERNAME` with your GitHub username. Do not paste passwords or access tokens into project files or chat.

## Notes

- If Git asks for your author name and email, set your preferred Git identity locally before committing.
- Keep generated video/audio exports out of the repository; `.gitignore` already excludes common large media files.
- The reference channel screenshots are deliberately not included.
