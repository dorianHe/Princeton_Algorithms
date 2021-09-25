from solution import Point


class BruteCollinearPoints:
    def __init__(self, data):
        self.point_lst = [Point(x, y) for x, y in data]

    def segments(self):
        segment_lst = []
        if len(self.point_lst) < 4:
            return segment_lst
        for i in range(len(self.point_lst)):
            for j in range(i+1, len(self.point_lst)):
                for p in range(j+1, len(self.point_lst)):
                    for q in range(p+1, len(self.point_lst)):
                        i_j_slope = self.point_lst[i].slope_to(self.point_lst[j])
                        i_p_slope = self.point_lst[i].slope_to(self.point_lst[p])
                        i_q_slope = self.point_lst[i].slope_to(self.point_lst[q])
                        if i_j_slope == i_p_slope and i_p_slope == i_q_slope:
                            segment_lst.append([i, q])
        return segment_lst

    def number_of_segments(self):
        return len(self.segments())


class SortCollinearPoints:
    def __init__(self, data):
        self.point_lst = [Point(x, y) for x, y in data]

    def segments(self):
        used_point_set = set()
        segment_lst = []
        if len(self.point_lst) < 4:
            return segment_lst
        for i in range(len(self.point_lst)):
            if self.point_lst[i] in used_point_set:
                continue
            origin = self.point_lst[i]
            slope_sorted_point_lst = sorted(self.point_lst, key=lambda x: x.slope_to(origin))
            for j in range(i+1, len(slope_sorted_point_lst)):
                if self.__four_slope_equal(origin, slope_sorted_point_lst[j:j+3]):
                    segment_lst.append(i)
                    segment_lst.append(j+2)
                    used_point_set.add(origin)
                    for point in slope_sorted_point_lst[j:j+3]:
                        used_point_set.add(point)
        return segment_lst

    def __four_slope_equal(self, point, slope_lst):
        if len(slope_lst) < 3:
            return False
        return point.slope_to(slope_lst[0]) == point.slope_to(slope_lst[1]) == point.slope_to(slope_lst[2])

    def number_of_segments(self):
        return len(self.segments())
