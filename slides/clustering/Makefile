all:
	echo $<

run: 
	reveal-md SubspaceProjections.md --disable-auto-open

static:
	reveal-md SubspaceProjections.md --static \
		--static-dirs=drawings,audio \
		--css chalkboard.css

zip:
	tar -cvzf static.tgz _static
