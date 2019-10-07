.PHONY: test prod clean


db.sqlite:
	python create.py

table.csv:
	python csv_transform.py

test: db.sqlite
	python test.csv

prod: db.sqlite table.csv
	./load_data.sh

clean:
	rm -f db.sqlite
	rm -f table.csv
