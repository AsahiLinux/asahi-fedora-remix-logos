NAME = asahi-fedora-remix-logos
XML = backgrounds/desktop-backgrounds-fedora.xml

all: bootloader/fedora.icns

VERSION := $(shell awk '/Version:/ { print $$2 }' $(NAME).spec)
RELEASE := $(shell awk '/Release:/ { print $$2 }' $(NAME).spec | sed 's|%{?dist}||g')
TAG=$(NAME)-$(VERSION)-$(RELEASE)

bootloader/fedora.icns: pixmaps/fedora-logo-small.png
	png2icns bootloader/fedora.icns pixmaps/fedora-logo-small.png

bootloader/bootlogo_128.png: pixmaps/fedora-logo-sprite.svg
	convert -background none -resize 128x128 -gravity center -extent 128x128 pixmaps/fedora-logo-sprite.svg bootloader/bootlogo_128.png
	zopflipng -ym bootloader/bootlogo_128.png bootloader/bootlogo_128.png

bootloader/bootlogo_256.png: pixmaps/fedora-logo-sprite.svg
	convert -background none -resize 256x256 -gravity center -extent 256x256 pixmaps/fedora-logo-sprite.svg bootloader/bootlogo_256.png
	zopflipng -ym bootloader/bootlogo_256.png bootloader/bootlogo_256.png

tag:
	@git tag -a -f -m "Tag as $(TAG)" -f $(TAG)
	@echo "Tagged as $(TAG)"

archive: tag
	@git archive --format=tar --prefix=$(NAME)-$(VERSION)/ HEAD > $(NAME)-$(VERSION).tar
	@bzip2 -f $(NAME)-$(VERSION).tar
	@echo "$(NAME)-$(VERSION).tar.bz2 created"
	@sha1sum $(NAME)-$(VERSION).tar.bz2 > $(NAME)-$(VERSION).sha1sum
	@echo "Everything done"

clean:
	rm -f *~ *bz2 bootloader/fedora.icns bootloader/bootlogo_128.png bootloader/bootlogo_256.png
