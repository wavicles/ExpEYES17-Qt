UI_FILES = $(shell ls *.ui)
UI_COMPILED = $(patsubst %.ui, ui_%.py, $(UI_FILES))
RC_FILES = $(shell ls *.qrc)
RC_COMPILED = $(patsubst %.qrc, %_rc.py, $(RC_FILES))

PYUIC = pyuic4
PYRCC = pyrcc4

all: $(UI_COMPILED) $(RC_COMPILED)

clean:
	rm -f $(UI_COMPILED) $(RC_COMPILED)
	rm -rf *.pyc *~ __pycache__

ui_%.py:  %.ui
	$(PYUIC) $< -o $@

%_rc.py: %.qrc
	$(PYRCC) $< -o $@

.PHONY: all clean
