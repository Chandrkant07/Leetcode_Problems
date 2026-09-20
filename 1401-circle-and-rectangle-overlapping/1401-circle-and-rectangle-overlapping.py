class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest x-coordinate on the rectangle to the circle's center
        closest_x = max(x1, min(xCenter, x2))
        
        # Find the closest y-coordinate on the rectangle to the circle's center
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate the squared Euclidean distance between the circle's center and this closest point
        distance_x = xCenter - closest_x
        distance_y = yCenter - closest_y
        squared_distance = (distance_x ** 2) + (distance_y ** 2)
        
        # If the squared distance is less than or equal to the squared radius, they overlap
        return squared_distance <= (radius ** 2)
