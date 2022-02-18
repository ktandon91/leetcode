class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = abs(ax1-ax2) * abs(ay1-ay2)
        area_b = abs(bx2-bx1) * abs(by1-by2)
        
        common_y = min(ay2, by2)-max(ay1, by1)
        if common_y < 0:
            common_y = 0
        common_x = min(ax2, bx2)-max(ax1, bx1)
        if common_x < 0:
            common_x = 0
        common_area = common_x * common_y
        return area_a + area_b - common_area
    # def computeArea(self, A, B, C, D, E, F, G, H):
    #     overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
    #     return (A-C)*(B-D) + (E-G)*(F-H) - overlap
