def check_piece_size(piece_size, s):
    n_pieces = int(len(s)/piece_size)
    for piece_idx in range(piece_size):
        base_piece = s[piece_idx]
        for piece in range(1,n_pieces):
            if base_piece != s[piece*piece_size+piece_idx]:
                return False
    return True

def solution(s):
    # Your code here
    for piece_size in range(1, int(len(s)/2)+1):
        if ((len(s)%piece_size) != 0): continue
        check = check_piece_size(piece_size, s)
        if check:
            return len(s)/piece_size
            
    return 1
            
    