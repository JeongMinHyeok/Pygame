import pygame

# pygame을 실행할때는 init(), 종료할때는 quit()을 꼭 적어줘야 함!
pygame.init()

#창 크기 지정
background = pygame.display.set_mode((480, 360))
#창 이름 지정
pygame.display.set_caption('PYGAME_1')

# 
fps = pygame.time.Clock()

# 화면 가운데 부터 시작하도록 x, y 좌표 설정
x_pos = background.get_size()[0]//2 # 240
y_pos = background.get_size()[1]//2 # 180


to_x = 0
to_y = 0

# boolean 함수를 생성해 while문 작성
play = True
while play:
    deltatime = fps.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #game의 event type이 QUIT 명령이라면
            play = False # while문을 종료시킴
        if event.type == pygame.KEYDOWN: #game의 event type이 키보드를 누른 상태일 때
            if event.key == pygame.K_UP:
                to_y = -1 # 좌표를 직접 변화시키지 않고 변수에 저장해 두었다가
            elif event.key == pygame.K_DOWN:
                to_y = 1
            elif event.key == pygame.K_RIGHT:
                to_x = 1
            elif event.key == pygame.K_LEFT:
                to_x = -1
        if event.type == pygame.KEYUP:
            to_x = 0
            to_y = 0
            # if event.key == pygame.K_UP:
            #     to_y = 0
            # elif event.key == pygame.K_DOWN:
            #     to_y = 0
            # elif event.key == pygame.K_RIGHT:
            #     to_x = 0
            # elif event.key == pygame.K_LEFT:
            #     to_x = 0
                
    # 변수 저장값을 좌표에 누적해주는 방식으로 접근
    x_pos += to_x
    y_pos += to_y
                
    # 항상 배경 - 이미지(도형) 순으로 코드를 작성해야 함! (반대로 하면 이미지가 배경에 덮여버림)
    background.fill((255,255,255)) # 배경색 : 흰색
    pygame.draw.circle(background, (255,0,0), (x_pos, y_pos), 5) # 4개의 인자 순서대로 (위치, 색깔, 중심점, 반지름)
    pygame.display.update() # 현재 화면 상태를 업데이트

pygame.quit()