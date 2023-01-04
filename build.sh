# -------------------------------------------------------------
# update the package on pypi
#
# Tip: if you don't want to retype pypi's username every time
#      define it as an environement variable (TWINE_USERNAME)
# -------------------------------------------------------------
function warn {
    GREEN='\033[0;32m'
    NORMAL='\033[0m'
    echo -e "${GREEN}$1${NORMAL}"
}

setup="python3 setup.py"
package_name=$($setup --name)
package_version=$($setup --version)

warn "BUILD ${package_name} (${package_version}) ON PYPI:"
warn "Cleaning up..."
rm -rf dist
rm -rf "${package_name}.egg-info"
warn "Recreating wheels..."
if python3 -m build; then
    warn "Done (${package_version})!"
else
    warn "Failed (${package_version})!"
fi
