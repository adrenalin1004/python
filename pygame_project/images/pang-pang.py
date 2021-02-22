import pygame
import random
import os 

#################################################################
# 기본 초기화
pygame.init()

#화면 크기 설정
screen_width  = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

print("화면 타이틀 ")

# 화면 타이틀 
pygame.display.set_caption("Pang Pang")  

# FPS 설정
clock = pygame.time.Clock()
#################################################################


# 1. 사용자 게임 초기화 (배경화면, 케릭터, 좌표, 속도, 폰트...)

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 이미지
background = pygame.image.load(os.path.join(image_path, "bkground.jpg"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(os.path.join(image_path, "00.png"))
character_size = character.get_rect().size #이미지크기
character_width = character_size[0]
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 중간
character_y_pos = screen_height  - character_height - stage_height

#이동할 좌표 
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.5

# 무기
weapon = pygame.image.load(os.path.join(image_path, "weapon00.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 여러발 발사 가능
weapons = []
# 무기 속도
weapon_speed = 10

# 무기 만들기
ball_images = [
    pygame.image.load(os.path.join(image_path, "boom1.png")),
    pygame.image.load(os.path.join(image_path, "boom2.png")),
    pygame.image.load(os.path.join(image_path, "boom3.png")),
    pygame.image.load(os.path.join(image_path, "boom4.png"))]

ball_speed_y = [-18, -15, -12, -9]

balls = []

balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "ball_to_x" : 3,
    "ball_to_y" : -6,
    "init_spd_y" : ball_speed_y[0]})

weapon_to_remove = -1
ball_to_remove = -1

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 30

# 시간 계산
start_ticks = pygame.time.get_ticks()

# 게임 메시지 
game_result = "Game Over"


# 이벤트 루프
running = True
while running :
    dt = clock.tick(30) # 초당 프레임수
    #print('fps : ' + str(clock.get_fps()))

    # 2. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

            #     to_y -= character_speed
            # elif event.key == pygame.K_DOWN:
            #     to_y += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    # 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    #character_y_pos += to_y * dt

    # 가로경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    #천장에 닫으면 없어짐
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0 ]

    #공의 위치
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width: 
            ball_val["ball_to_x"] = ball_val["ball_to_x"] * -1

        # 공이 세로 위치
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["ball_to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["ball_to_y"] += 0.5  

        ball_val["pos_x"] += ball_val["ball_to_x"]
        ball_val["pos_y"] += ball_val["ball_to_y"]


    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        if character_rect.colliderect(ball_rect):
            running = False
            break
        
        #공과 무기 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_x_pos = weapon_val[0]
            weapon_y_pos = weapon_val[1]
            #무기 위치정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos


            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # 무기 이미지 없애기
                ball_to_remove = ball_idx # 공 이미지 없애기
                
                # 작은공으로 나뉘기
                if ball_img_idx < 3:
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]


                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1,
                        "ball_to_x" : -3,
                        "ball_to_y" : -6,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]})

                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1,
                        "ball_to_x" : 3,
                        "ball_to_y" : -6,
                        "init_spd_y" : ball_speed_y[0]})
                break

    # 충돌된 공, 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 모든 공을 없앤 경우
    if len(balls) == 0:
        game_result = "Mission Clear"
        running = False

    # 충동 케크
    if character_rect.colliderect(ball_rect):
        print("충돌했어요")
        running = False


   # 5. 화면에 그리기
    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    
    screen.blit(stage, (0,screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))



    # 경과 시간
    elapsed_time = ( pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,0,0))
    screen.blit(timer, (400,10))

    # 시간이 0이면 게임 종료
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False 

    
    pygame.display.update() #게임화면을 다시 그리기!

msg = game_font.render(game_result, True, (255,0,0))
msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()
pygame.time.delay(2000)
    
# game 종료
pygame.quit()
