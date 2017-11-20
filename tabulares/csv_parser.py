with open('episodios.csv') as csv_files:
    samurai = csv_files.readlines()

parserd_samurai = list(map(lambda x: x.strip().split(';'), samurai))
