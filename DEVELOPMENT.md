# Development Environment Setup

**⚠️ IMPORTANT: Choose ONE of these setup options below.**

## 🌟 Option 1: GitHub Codespaces (Easiest)

1. Fork this repository to your GitHub account
2. Go to your forked repo on GitHub.com
3. Click "Code" → "Codespaces" → "Create codespace on main"
4. Wait 2-3 minutes for automatic setup
5. Run: `streamlit run examples/day_1_example.py`

## 🔧 Option 2: VS Code with Dev Container (Local with Docker)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Install VS Code + "Dev Containers" extension
3. Open this folder in VS Code
4. Click "Reopen in Container" when prompted
5. Wait for container to build
6. Run: `streamlit run examples/day_1_example.py`

## 🐍 Option 3: Local Python Setup (No Docker)

```bash
# Install Python packages locally
pip install -r requirements.txt

# Test your setup
streamlit run examples/day_1_example.py
```

## � Quick Commands

Once your environment is ready:

```bash
# Run examples
streamlit run examples/day_1_example.py

# Work on lessons
streamlit run lessons/day_1.py
```

Your Streamlit app will be available at `http://localhost:8501`

## ✅ Testing Your Setup

Run any example to verify everything works:
```bash
streamlit run examples/day_1_example.py
```

If you see the Streamlit interface in your browser, you're all set!

---

**For Students:** GitHub Codespaces is recommended for the easiest setup experience.  
**For Instructors:** All environments are configured identically for consistent troubleshooting.
