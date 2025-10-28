# 🚀 Deploy to GitHub Pages

## Quick Setup

1. **Push your changes to GitHub:**
```bash
git push origin main
```

2. **Enable GitHub Pages:**
   - Go to: https://github.com/v-hansen/algorithms/settings/pages
   - Under "Source", select: **Deploy from a branch**
   - Under "Branch", select: **main** and **/ (root)**
   - Click **Save**

3. **Wait 1-2 minutes** for deployment

4. **Access your site:**
   - URL: https://v-hansen.github.io/algorithms/
   - The `index.html` will be served automatically

## Verify Deployment

Check deployment status at:
https://github.com/v-hansen/algorithms/deployments

## Update Site

Every time you push to `main`, GitHub Pages will automatically rebuild:
```bash
git add .
git commit -m "Update site"
git push origin main
```

## Custom Domain (Optional)

To use a custom domain:
1. Add a `CNAME` file with your domain
2. Configure DNS settings
3. Enable HTTPS in GitHub Pages settings

## Troubleshooting

**Site not loading?**
- Check Settings > Pages is enabled
- Verify branch is set to `main` and root `/`
- Wait a few minutes after first setup

**404 Error?**
- Ensure `index.html` is in the root directory ✅
- Check file name is exactly `index.html` (case-sensitive)

**Changes not showing?**
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Wait 1-2 minutes for GitHub to rebuild
- Check Actions tab for build status
