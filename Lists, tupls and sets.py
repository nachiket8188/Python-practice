# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses_2 = ['Phy. Ed.', 'Social Science']
#
# print(courses)
# print(len(courses))
# print(courses[3])
# print(courses[-4])
# print(courses[0:2])
# print(courses[:2])
# print(courses[2:])
#
# courses.append('Art')
# print(courses)
#
# courses.insert(0, 'Geography')
# print(courses)
#
# courses.insert(0, courses_2)
# print(courses)
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.extend(courses_2)
# print(courses)

# courses.remove('Math')
# print(courses)
# popped = courses.pop()
# print(courses)
# print(popped)

# courses.reverse()
# print(courses)
# courses.sort()
# print(courses)
#
# nums = [1, 5, 4, 3]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
#
# print(sorted(nums))
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# print(courses)
# print(courses.index('CompSci'))
# print('Art' in courses)
#
# for index, item in enumerate(courses, start=1):
#     print(index, item)
#
# course_string = ' - '.join(courses)
# print(course_string)
# new_list = course_string.split(' - ')
# print(new_list)

# Tuples

tuple_1 = ('History', 'Math', 'Physics', 'CompSci') # Unlike lists, tuples are immutable i.e. cannot be changed.
tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)
# tuple_1[0] = 'Art'

# Sets

set = {'History', 'Math', 'Physics', 'CompSci', 'Math'} # Unlike lists & tuples, sets do not have order and doesn't allow duplicates.
set_2 = {'History', 'Math', 'Art', 'Design'}
print(set)
# Membership tests are more efficient in case of sets when compared to lists ot tuple. They're optimized for this.
print('Math' in set)
print(set_2.intersection(set))
print(set_2.difference(set))
print(set_2.union(set))

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # This isn't right! It's a dict !
empty_set = set()