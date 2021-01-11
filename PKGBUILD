depends=('bash>=4.4' 'gnupg>=2.2' 'curl>=7.72' 'Uniglot')
makedepends=('make>=4.2')
checkdepends=()
optdepends=()
pkgname="$(git config remote.origin.url | rev | cut -f 1 -d '/' | rev | sed 's/.git$//')"
pkgver="$(git describe --tag --abbrev=0)"."$(git rev-parse --short HEAD)"
pkgrel=1
pkgrel() { 
    echo $(( `git log "$(git describe --tag --abbrev=0)"..HEAD | grep -c commit` + 1 ))
}
epoch="$(git log | grep -c commit)"
pkgdesc="$(head -n 1 README.md)"
arch=("x86_64")
url="$(git config remote.origin.url | sed 's/.git$//')"
license=('custom')
groups=()
provides=("${pkgname}")
conflicts=()
replaces=("${pkgname,,}", "aninix-${pkgname,,}")
backup=()
options=()
install=
changelog=
source=()
noextract=()
md5sums=()
validpgpkeys=()

prepare() {
    git pull
}

build() {
    make -C ..
}

check() {
    chmod -R u+r ../pkg
	make -C .. test
}

package() {
    export pkgdir="${pkgdir}"
	make -C .. install
    install -D -m644 ../LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
