# GitHub Contribution Graph Activity

<div align="center">
  <h2>Before</h2>
  <img src="/images/before.png" alt="Before" width = "1000">
</div>   

<div align="center">
  <h2>After</h2>
  <img src="/images/after.png" alt="After" width = "1000">
</div>   

<h1>How to use</h1>

<p>
  1. Make a private repo on GitHub.
</p>

<p>
  2. Run the python script (commit_generator.py) in your new private repo.
</p>

<div align="center">
  <img src="/images/cli.png" alt="CLI">
</div>

<p>
  3. Enter a year (e.g., 2020) and a commit frequency (or press Enter for default ~70%).
</p>
 
<p>
  4. Wait for commits to generate and push, then refresh your GitHub profile to see the updated contribution graph.
</p>

<h1>Note</h1>

<p>This is reversible. If you make a mistake, deleting this private repo will remove the commit activity from your GitHub contribution graph.</p>

<p>This script is for educational purposes, it should not be used to misrepresent professional contributions or coding activity.</p>

<h1>System requirements</h1>
You need to have Python and Git installed to be able to execute the script.

<h1>How it works</h1>

<h2>User Input Collection</h2>
  <ul>
    <li>The user is prompted to enter a year (between 1970 and the current year).</li>
    <li>The user specifies the commit frequency (1% to 100%) or accepts the default (~70%).</li>
  </ul>

<h2>Commit Generation</h2>
<ul>
    <li>The script iterates through every day of the selected year.</li>
    <li>For each day, it randomly decides (based on the percentage) whether a commit will be made.</li>
    <li>If a commit is made, it:
      <ul>
        <li>Creates/modifies a temporary file (<code>temp.txt</code>).</li>
        <li>Stages (<code>git add</code>), commits (<code>git commit</code> with a timestamp), and pushes (<code>git push</code>).</li>
        <li>Generates 1 to 4 commits per day to vary contribution intensity.</li>
      </ul>
    </li>
</ul>

<h2>Pushing to GitHub</h2>
  <ul>
    <li>Once all commits are generated, the script pushes them to GitHub.</li>
    <li>It then removes <code>temp.txt</code> and makes a final commit to clean up.</li>
  </ul>

<h1>Troubleshooting</h1>
1. It takes several minutes for GitHub to update your contribution graph. Check if the repo has any new commits and wait a couple of minutes.

2. Are you using a private repository? If so, enable showing private contributions following [this guide](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/showing-your-private-contributions-and-achievements-on-your-profile).

3. Make sure your GitHub email is the same as the one in your local git config settings. GitHub only counts contributions when they are made using the same email.

```
git config --get user.email # check your local email address
```

```
git config --global user.email "user@example.com" # update your email address
```

Create a new repository and rerun the script.
