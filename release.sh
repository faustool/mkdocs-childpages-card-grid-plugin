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
package_version=v$($setup --version) # add a 'v' in front (git convention) 

if test -d "./dist"; then
    warn "RELEASE ${package_name} (${package_version}) ON PYPI:"
    warn "Upload to Pypi..."
    if twine upload -r pypi dist/* ; then
        warn "... create tag ${package_version}, and push to remote git repo..."
        warn "$ git tag ${package_version}"
        warn "$ git push --tags"
        warn "Done (${package_version})!"
    else
        warn "Failed (${package_version})!"
    fi
else
    warn "No ./dist directory found; run build.sh first!"
fi