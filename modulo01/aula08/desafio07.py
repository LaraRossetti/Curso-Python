import pygame
import emoji

pygame.init()
caminhoArquivo = 'C:\\Users\\larar\\Desktop\\Cursos\\Curso Python\\modulo01\\aula08\\desafio07.mp3'
pygame.mixer.music.load(caminhoArquivo)
print(emoji.emojize('AVENGERS, ASSEMBLE!!!!!!! :dagger: :bomb: :bow_and_arrow: :crossed_swords: :shield: :firecracker: :fire: :flexed_biceps: :index_pointing_at_the_viewer: :collision: :face_with_symbols_on_mouth:' ))
pygame.mixer.music.play()
input()
pygame.event.wait()