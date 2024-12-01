def get_final_titles(titles):
    final_titles = []
    for word in titles:
        if not word[0].isupper():
            final_titles.append(word.capitalize())
    final_titles.append('')
    return " ".join(final_titles)

if __name__ == "__main__":
    titles = input()
    titles = titles.split(' ')
    final_titles = get_final_titles(titles)
    print(final_titles)
    print(len(final_titles))