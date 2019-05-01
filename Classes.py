class Piece(object):

    fromLettertoNumb = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }

    fromNumbtoLetter = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h"
    }

    def __init__(self, player, value, pos, image):
        self.player = player
        self.value = value
        self.numberOfmoves = 0
        self.pos = pos
        self.image = image

class Pawn(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 1, pos, image)

    def moves(self, chessBoard):

        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        solutionMoves = []

        if self.player == 'black':
            try:
                temp = chessBoard[row + 1][column]
                solutionMoves.append([row + 1, column])
            except:
                pass
            try:
                temp = chessBoard[row + 1][column + 1]
                if chessBoard[row + 1][column + 1] != 0:
                    solutionMoves.append([row + 1, column + 1])
            except:
                pass
            try:
                temp = chessBoard[row + 1][column - 1]
                if chessBoard[row + 1][column - 1] != 0:
                    solutionMoves.append([row + 1, column - 1])
            except:
                pass
            try:
                temp = chessBoard[row + 2][column]
                if self.numberOfmoves == 0:
                    solutionMoves.append([row+2],[column])
            except:
                pass
        if self.player == 'white':
            try:
                temp = chessBoard[row - 1][column]
                solutionMoves.append([row - 1, column])
            except:
                pass
            try:
                temp = chessBoard[row - 1][column + 1]
                if chessBoard[row - 1][column + 1] != 0:
                    solutionMoves.append([row - 1, column + 1])
            except:
                pass
            try:
                temp = chessBoard[row - 1][column - 1]
                if chessBoard[row - 1][column - 1] != 0:
                    solutionMoves.append([row - 1, column - 1])
            except:
                pass
            try:
                temp = chessBoard[row - 2][column]
                if self.numberOfmoves == 0:
                    solutionMoves.append([row-2],[column])
            except:
                pass
        # get rid of negative indexes
        temp = [i for i in solutionMoves if i[0] >= 0 and i[1] >= 0]
        allPossibleMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
        allPossibleMoves.sort()

        return allPossibleMoves


class Rook(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 7, pos, image)

    def moves(self, chessBoard):
        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        i, j = row, column
        solutionMoves = []

        for j in range(row, 0, -1):
            if j != column:
                if chessBoard[row][j] != 1:
                    break
                solutionMoves.append((row, j))

        for j in range(row, 8, 1):
            if j != column:
                if chessBoard[row][j] != 1:
                    break
                solutionMoves.append((row, j))

        for i in range(column, 0, -1):
            if i != row:
                if chessBoard[i][column] != 1:
                    break
                solutionMoves.append((i, column))
        for i in range(column, 8, 1):
            if i != row:
                if chessBoard[i][column] != 1:
                    break
                solutionMoves.append((i, column))

        solutionMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in solutionMoves]
        solutionMoves.sort()
        return solutionMoves


class Queen(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 9,  pos, image)

    def moves(self, chessBoard):
        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        i, j = row, column
        solutionMoves = []

        for i in range(row, -1, -1):
            if i != row:
                j = j - 1
                if chessBoard[i][j] != 1:
                    break
                if j >= 0:
                    solutionMoves.append((i, j))

        i, j = row, column

        for i in range(row, 8, 1):
            if i != row:
                j = j + 1
                if chessBoard[i][j] != 1:
                    break
                if j < 8:
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, -1, -1):
            if i != row:
                j = j + 1
                if j >= 0:
                    if chessBoard[i][j] != 1:
                        break
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, 8, 1):
            if i != row:
                j = j - 1
                if j >= 0:
                    if chessBoard[i][j] != 1:
                        break
                    solutionMoves.append((i, j))

        i, j = row, column
        for j in range(row, 0, -1):
            if j != column:
                if chessBoard[row][j] != 1:
                    break
                solutionMoves.append((row, j))

        for j in range(row, 8, 1):
            if j != column:
                if chessBoard[row][j] != 1:
                    break
                solutionMoves.append((row, j))

        for i in range(column, 0, -1):
            if i != row:
                if chessBoard[i][column] != 1:
                    break
                solutionMoves.append((i, column))
        for i in range(column, 8, 1):
            if i != row:
                if chessBoard[i][column] != 1:
                    break
                solutionMoves.append((i, column))

        solutionMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in solutionMoves]
        solutionMoves.sort()

        return solutionMoves


class King(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 10, pos, image)

    def moves(self, chessBoard):

        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        possibleMoves = []
        try:
            temp = chessBoard[row + 1][column]
            possibleMoves.append([row + 1, column])
        except:
            pass
        try:
            temp = chessBoard[row - 1][column]
            possibleMoves.append([row - 1, column])
        except:
            pass
        try:
            temp = chessBoard[row][column + 1]
            possibleMoves.append([row, column + 1])
        except:
            pass
        try:
            temp = chessBoard[row][column - 1]
            possibleMoves.append([row, column - 1])
        except:
            pass
        try:
            temp = chessBoard[row - 1][column - 1]
            possibleMoves.append([row - 1, column - 1])
        except:
            pass
        try:
            temp = chessBoard[row + 1][column + 1]
            possibleMoves.append([row + 1, column + 1])
        except:
            pass
        try:
            temp = chessBoard[row - 1][column + 1]
            possibleMoves.append([row - 1, column + 1])
        except:
            pass
        try:
            temp = chessBoard[row + 1][column - 1]
            possibleMoves.append([row + 1, column - 1])
        except:
            pass

        temp = [i for i in possibleMoves if i[0] >= 0 and i[1] >= 0]
        allPossibleMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
        allPossibleMoves.sort()

        return allPossibleMoves


class Bishop(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 5, pos, image)

    def moves(self, chessBoard):

        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        i, j = row, column
        solutionMoves = []

        for i in range(row, -1, -1):
            if i != row:
                j = j - 1
                if chessBoard[i][j] != 1:
                    break
                if j >= 0:
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, 8, 1):
            if i != row:
                j = j + 1
                if chessBoard[i][j] != 1:
                    break
                if j < 8:
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, -1, -1):
            if i != row:
                j = j + 1
                if j >= 0:
                    if chessBoard[i][j] != 1:
                        break
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, 8, 1):
            if i != row:
                j = j - 1
                if j >= 0:
                    if chessBoard[i][j] != 1:
                        break
                    solutionMoves.append((i, j))

        solutionMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in solutionMoves]
        solutionMoves.sort()

        return solutionMoves


class Knight(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 5, pos, image)

    def moves(self, chessBoard):

        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        possibleMoves = []

        try:
            temp = chessBoard[row + 1][column - 2]
            possibleMoves.append([row + 1, column - 2])
        except:
            pass
        try:
            temp = chessBoard[row + 2][column - 1]
            possibleMoves.append([row + 2, column - 1])
        except:
            pass
        try:
            temp = chessBoard[row + 2][column + 1]
            possibleMoves.append([row + 2, column + 1])
        except:
            pass
        try:
            temp = chessBoard[row + 1][column + 2]
            possibleMoves.append([row + 1, column + 2])
        except:
            pass
        try:
            temp = chessBoard[row - 1][column + 2]
            possibleMoves.append([row - 1, column + 2])
        except:
            pass
        try:
            temp = chessBoard[row - 2][column + 1]
            possibleMoves.append([row - 2, column + 1])
        except:
            pass
        try:
            temp = chessBoard[row - 2][column - 1]
            possibleMoves.append([row - 2, column - 1])
        except:
            pass
        try:
            temp = chessBoard[row - 1][column - 2]
            possibleMoves.append([row - 1, column - 2])
        except:
            pass

        temp = [i for i in possibleMoves if i[0] >= 0 and i[1] >= 0]
        allPossibleMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
        allPossibleMoves.sort()
        print(allPossibleMoves)
        return allPossibleMoves


class ComputerMoves(Pawn,Rook,Queen,Bishop,King):

    #def __init__(self,player,pos):


    def getdangerpieces(self):
        allPossibleMoves = Pawn.moves(Pawn)
        allPossibleMoves.extend(Rook.moves(Rook))
        allPossibleMoves.extend(Queen.moves(Queen))
        allPossibleMoves.extend(Bishop.moves(Bishop))
        allPossibleMoves.extend(King.moves(King))
        allPossibleMoves.extend(Knight.moves(Knight))
        return allPossibleMoves










