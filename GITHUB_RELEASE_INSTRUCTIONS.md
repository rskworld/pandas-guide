# GitHub Release Creation Instructions

<!--
Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
-->

## ✅ Completed Steps

1. ✅ Code pushed to GitHub repository: https://github.com/rskworld/pandas-guide.git
2. ✅ Tags created and pushed:
   - `v1.0.0` - Main release tag
   - `v1.0.0-beta` - Beta release tag
3. ✅ Release notes created in `RELEASE_NOTES.md`

## 📦 Create GitHub Releases

You have two options to create releases:

### Option 1: Using GitHub Web Interface (Recommended)

1. Go to your repository: https://github.com/rskworld/pandas-guide
2. Click on **"Releases"** in the right sidebar (or go to https://github.com/rskworld/pandas-guide/releases)
3. Click **"Create a new release"**
4. For **v1.0.0** release:
   - **Choose a tag**: Select `v1.0.0` from dropdown
   - **Release title**: `Pandas Data Manipulation Guide v1.0.0`
   - **Description**: Copy content from `RELEASE_NOTES.md` (Version 1.0.0 section)
   - **Set as latest release**: ✅ Check this
   - Click **"Publish release"**

5. For **v1.0.0-beta** release (optional):
   - **Choose a tag**: Select `v1.0.0-beta`
   - **Release title**: `Pandas Data Manipulation Guide v1.0.0-beta`
   - **Description**: Copy content from `RELEASE_NOTES.md` (Beta section)
   - **Set as pre-release**: ✅ Check this
   - Click **"Publish release"**

### Option 2: Using PowerShell Script (Automated)

1. Generate a GitHub Personal Access Token:
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Select scopes: `repo` (full control of private repositories)
   - Copy the token

2. Run the PowerShell script:
```powershell
.\create_release.ps1 -Version "v1.0.0" -Token "your_github_token_here"
```

For beta release:
```powershell
.\create_release.ps1 -Version "v1.0.0-beta" -Token "your_github_token_here" -IsPrerelease "true"
```

### Option 3: Using GitHub CLI (if installed)

```bash
# Install GitHub CLI first: https://cli.github.com/
gh release create v1.0.0 --title "Pandas Data Manipulation Guide v1.0.0" --notes-file RELEASE_NOTES.md

gh release create v1.0.0-beta --title "Pandas Data Manipulation Guide v1.0.0-beta" --notes-file RELEASE_NOTES.md --prerelease
```

## 📋 Release Information

### v1.0.0 Release Details:
- **Tag**: v1.0.0
- **Type**: Stable Release
- **Features**: 
  - 8 comprehensive Jupyter notebooks
  - Sample data files
  - Example scripts
  - Complete documentation
  - Advanced operations guide

### v1.0.0-beta Release Details:
- **Tag**: v1.0.0-beta
- **Type**: Pre-release
- **Features**: Same as v1.0.0 (beta version)

## 🔗 Quick Links

- Repository: https://github.com/rskworld/pandas-guide
- Releases Page: https://github.com/rskworld/pandas-guide/releases
- Tags: https://github.com/rskworld/pandas-guide/tags

## 📝 Notes

- All code has been successfully pushed to the main branch
- Tags are already created and pushed
- You just need to create the releases using one of the methods above
- The release notes are ready in `RELEASE_NOTES.md`

