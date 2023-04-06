def reverse_words(input):
    str=input.split()
    rstr = str[::-1]
    output=' '.join(rstr)
    print('Input string is\n\n',input,'\n\nOuput string is\n\n',output)
    




def main():
    reverse_words('Two roads diverged in a yellow wood, And sorry I could not travel both Andbe one traveler, long I stood And looked down one as far as I could To whereit bent in the undergrowth')
    reverse_words('Then took the other, as just as fair, And having perhaps the better claim,Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,')
 

if __name__ == '__main__':

 

    main()
