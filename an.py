def log_alder():
    try:
        alder = int(input("Hvor gammel er du? "))

        if 0 <= alder <= 20:
            gruppe = "0-20 år"
        elif 21 <= alder <= 50:
            gruppe = "21-50 år"
        elif 51 <= alder <= 100:
            gruppe = "51-100 år"
        elif alder >= 101:
            gruppe = "101+ år"
        else:
            print("Ugyldig alder!")
            return

        with open("alder_logg.txt", "a") as fil:
            fil.write(f"Alder: {alder} - Gruppe: {gruppe}\n")

        print(f"Du er i aldersgruppen: {gruppe}")
    except ValueError:
        print("Vennligst skriv inn et gyldig tall!")

log_alder()