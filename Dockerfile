FROM python:latest

WORKDIR /usr/app/src

COPY . .

CMD python3 ./get_three_word_sequences.py moby-dick.txt moby_dick.txt origin_of_species.txt ; cat moby_dick.txt | python3 ./get_three_word_sequences.py