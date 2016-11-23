RM=rm -rf
DESTDIR=$(SR_CODE_BASE)/snaproute/src/out/bin
MKDIR=mkdir -p
RSYNC=rsync -rupE

COMP_NAME=sdk
SRCS=flexswitchV2.py\
	  flexprint.py\
	  flexprintV2.py

all: install 
install:
	@$(MKDIR) $(DESTDIR)/sdk/py/
	install $(SRCS) $(DESTDIR)/sdk/py/

guard:
ifndef SR_CODE_BASE
	 $(error SR_CODE_BASE is not set)
endif

clean:guard
	 @echo "Cleaning $(RM) $(DESTDIR)/sdk/py"
	 $(RM) $(DESTDIR)/sdk/py
