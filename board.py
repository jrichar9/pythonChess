import pygame
import Pieces

class Board(object):

    def printBoard( board, highlights, screen):
        brown_square = pygame.image.load("images/brown_square.png")
        white_square = pygame.image.load("images/white_square.png")
        cyan_square = pygame.image.load("images/cyan_square.png")
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    screen.blit(white_square, (j*100+50, i*50))
                else:
                    screen.blit(white_square, (j*100, i*50))
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    screen.blit(brown_square, (j*100, i*50))
                else:
                    screen.blit(brown_square, (j*100+50, i*50))
        if highlights != (0,0):
            for tile in highlights:
                screen.blit(cyan_square,tile)
        for piece in board:
                screen.blit(piece.image, piece.pos)


    def loadImages():
        # load images and set the logo
        logo = pygame.image.load("images/brown_square.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("chess v0.1")

        black_king = pygame.image.load("images/black_king.png")
        black_queen = pygame.image.load("images/black_queen.png")
        black_bishop = pygame.image.load("images/black_bishop.png")
        black_knight = pygame.image.load("images/black_knight.png")
        black_rook = pygame.image.load("images/black_rook.png")
        black_pawn = pygame.image.load("images/black_pawn.png")
        white_king = pygame.image.load("images/white_king.png")
        white_queen = pygame.image.load("images/white_queen.png")
        white_bishop = pygame.image.load("images/white_bishop.png")
        white_knight = pygame.image.load("images/white_knight.png")
        white_rook = pygame.image.load("images/white_rook.png")
        white_pawn = pygame.image.load("images/white_pawn.png")

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    '''
    bK = Pieces.King(0, 10, 'king', [200, 0], pygame.image.load("images/black_king.png"))
    bQ = Piece(0, 10, 'queen', [150, 0], pygame.image.load("images/black_queen.png"))
    bB1=Piece(0, 10, 'bishop', [100, 0],pygame.image.load("images/black_bishop.png"))
    bB2=Piece(0, 10, 'bishop', [250, 0],pygame.image.load("images/black_bishop.png"))
    bKn1=Piece(0, 10, 'knight', [300, 0], pygame.image.load("images/black_knight.png"))
    bKn2=Piece(0, 10, 'knight', [50, 0], pygame.image.load("images/black_knight.png"))
    bR1=Piece(0, 10, 'rook', [0, 0], pygame.image.load("images/black_rook.png"))
    bR2=Piece(0, 10, 'rook', [350, 0],pygame.image.load("images/black_rook.png"))
    bP1=Piece(0, 10, 'pawn', [0, 50], pygame.image.load("images/black_pawn.png"))
    '''
    bP1 = Pieces.Pawn('black',[0, 50])
    bP2 = Pieces.Pawn('black',[50, 50])
    bP3 = Pieces.Pawn('black',[100, 50])
    bP4 = Pieces.Pawn('black',[150, 50])
    bP5 = Pieces.Pawn('black',[200, 50])
    bP6 = Pieces.Pawn('black',[250, 50])
    bP7 = Pieces.Pawn('black',[300, 50])
    bP8 = Pieces.Pawn('black',[350, 50])

    board = [bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8]
    '''
    board = [[bR1, bKn1, bB1, bQ, bK, bB2, bKn2, bR2],
             [bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    '''
    Board.printBoard(board, (0,0), screen)
    pygame.display.flip()
    '''
    screen.blit(black_rook, (0, 0))
    screen.blit(black_knight, (50, 0))
    screen.blit(black_bishop, (100, 0))
    screen.blit(black_queen, (150, 0))
    screen.blit(black_king, (200, 0))
    screen.blit(black_bishop, (250, 0))
    screen.blit(black_knight, (300, 0))
    screen.blit(black_rook, (350, 0))
    for i in range(8):
        screen.blit(black_pawn, (i*50, 50))

    screen.blit(white_rook, (0, 350))
    screen.blit(white_knight, (50, 350))
    screen.blit(white_bishop, (100, 350))
    screen.blit(white_queen, (150, 350))
    screen.blit(white_king, (200, 350))
    screen.blit(white_bishop, (250, 350))
    screen.blit(white_knight, (300, 350))
    screen.blit(white_rook, (350, 350))
    for i in range(8):
        screen.blit(white_pawn, (i * 50, 300))


    pygame.display.flip()
    '''

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for piece in board:
                    print(piece.isClicked(pos))

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()