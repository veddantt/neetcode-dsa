class Solution(object):
    def diameterOfBinaryTree(self, root):
        class DiameterData(object):
            def __init__(self, diameter, height):
                self.diameter = diameter
                self.height = height

        def calculateDiameterAndHeight(root):
            if not root:
                return DiameterData(0, 0)

            leftData = calculateDiameterAndHeight(root.left)
            rightData = calculateDiameterAndHeight(root.right)

            currentDiameter = max(leftData.height + rightData.height,
                                  max(leftData.diameter, rightData.diameter))
            currentHeight = max(leftData.height, rightData.height) + 1

            return DiameterData(currentDiameter, currentHeight)

        data = calculateDiameterAndHeight(root)
        return data.diameter