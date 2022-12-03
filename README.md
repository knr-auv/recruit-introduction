# recruit-introduction
live training for recruits

## Preliminaries
- Access to this repository, member status in knr-auv organization
- [Visual Studio Code](https://code.visualstudio.com/) - Code Editor
- VSCode extensions listed in [wiki Styles](https://github.com/knr-auv/docs/wiki/Styles)
- [Conda](https://github.com/knr-auv/docs/wiki/Conda)

## Materials
- [Docs](https://github.com/knr-auv/docs) - styling configuration, conda installation, dual boot install...
- [Example of workflow](https://github.com/knr-auv/autonomy/pulls?q=) - you can check how actual workflow looks on work done by @miki87278 or @mpfmorawski, \
which was reviewed by @niemiaszek for autonomy repository.

## Scope of work

1. Make sure you have setup everything listed in [preliminaries](#preliminaries)
2. Prepare SSH key for your PC, so you can actually clone repos via ssh key and easily add your changes in knr-auv. \
Follow [this tutorial from GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
3. Add the key to your GitHub account. Again, [tutorial by Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
4. Check if your key was succesfully added, trying to [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository with SSH
5. Now its time for your main task. Your task will be "fixing" the `add-ugly-code` branch. \
It can be viewed via [GitHub](https://github.com/knr-auv/recruit-introduction/tree/add-ugly-code) or locally.
6. Firstly, [create remote branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) with naming `<your_nickname>/fix-ugly-code`. Make sure your new branch has `add-ugly-code` branch as a parent.
7. Then, pull your local repository, so it will be aware of your new branch existance. `git pull`
8. Once done, [checkout](https://git-scm.com/docs/git-checkout) to your new remote branch. You should see actual code appearing in your local directory.
9. Now you can work on actual fix. \
Try to fix problems suggested by PyLint. \
Try to apply _Black_ and _isort_ formatting (should work just by `ctrl+s` if you setup VSC extensions correctly). 
10. If you are happy with your fix, [stage and commit your changes with a message](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
11. Push your local changes to remote branch (just `git push`)
12. You should now see your changes on GitHub branch if everything went as planned. \
As a final step, open Pull Request from your branch to `main` and add @niemiaszek as a reviewer
