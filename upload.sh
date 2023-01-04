# -----------------------------------------------------------------------
# upload the package to pypi (main branch) or testpypi (any other branch)
# -----------------------------------------------------------------------
function warn {
    GREEN='\033[0;32m'
    NORMAL='\033[0m'
    echo -e "${GREEN}$1${NORMAL}"
}

setup="python3 setup.py"
package_name=$($setup --name)
package_version=$($setup --version)
branch=$(git rev-parse --abbrev-ref HEAD)

if test "$branch" == "main"; then
  pypi_repo="pypi" # only release to pypi.org from the main branch
else
  pypi_repo="testpypi" # any calls to this script outside the main branch will upload to test.pypi.org
fi

if test -d "./dist"; then
    warn "RELEASE ${package_name} (${package_version}) ON PYPI:"
    warn "Upload to Pypi..."
    if twine upload -r $pypi_repo dist/* ; then
        warn "Done (${package_version})!"
    else
        warn "Failed (${package_version})!"
    fi
else
    warn "No ./dist directory found; run build.sh first!"
fi
