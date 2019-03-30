PRGM = swaylock-fancy
PREFIX ?= /usr
SHRDIR ?= $(PREFIX)/share
BINDIR ?= $(PREFIX)/bin

install:
		@install -Dm755 lock.py        $(DESTDIR)$(BINDIR)/$(PRGM)
		@install -Dm755 lock.png       -t $(DESTDIR)$(SHRDIR)/$(PGRM)/icons
		@install -Dm644 LICENSE        -t $(DESTDIR)$(SHRDIR)/licenses/$(PRGM)

