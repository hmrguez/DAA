# Rule to watch Typst file
watch:
	typst watch $(filter-out $@,$(MAKECMDGOALS))/proof.typ

# Rule to clean up
clean:
	find . -type f -name '*.pdf' -delete

# Rule to test
test:
	@cd $(filter-out $@,$(MAKECMDGOALS)) && python -m unittest tests.py