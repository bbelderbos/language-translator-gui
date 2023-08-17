from db import store_translation, retrieve_translations
from translate import translate_text


def main():
    while True:
        destination = input("Enter target language (q to exit, p to print history): ")
        if destination == "q":
            print("Exiting...")
            break
        elif destination == "p":
            print("Translation History:")
            translations = retrieve_translations()
            for t in translations:
                print(t)
            continue

        while True:
            text = input("Enter text to translate (q to quit): ")
            if text == "q":
                break
            translated_text = translate_text(text, destination)
            print(translated_text)
            store_translation(text, destination, translated_text)


if __name__ == "__main__":
    main()
