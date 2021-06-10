# streamlit import
import streamlit as st

# create empty variables to suppress annoying name errors displaying on streamlit interface
rotation_count = ()
target_og = ()
rotation_lists = ()
total_batch_mass = ()
total_bbl_count = ()
target_bbl = ()
hot_liquor = ()
final_bbl = ()
total_batch_og = ()
final_og = ()

# create streamlit title and first input box
st.title('Liquor Back Calculator')

# noinspection PyRedeclaration
target_og = st.text_input("Enter your target gravity value (e.g, 12.0):")

# populate second text box and convert gravity to float
if target_og:
    target_og = float(target_og)
    try:
        rotation_count = float(st.text_input('How many rotations in this brew?:', help='Only 1 thru 4 rotations are supported'))
    except ValueError:
        pass

# populate third text box and create empty lists for # of rotation turns
if rotation_count:
    rotation_count = int(rotation_count)
    rotation_lists = [[] for i in range(rotation_count)]

# loop through empty lists and populate streamlit text box values to append into empty lists
for x in rotation_lists:
    if len(rotation_lists) == 1:
        try:
            first_rtn_OG = float(st.text_input('for the first brew rotation, what was the gravity reading?:'))
            first_rtn_bbl = float(st.text_input('for the first brew rotation, what was the barrel count?:'))
            rotation_lists[0].append(first_rtn_OG)
            rotation_lists[0].append(first_rtn_bbl)
        except ValueError:
            pass
        break
    elif len(rotation_lists) == 2:
        try:
            first_rtn_OG = float(st.text_input('for the first brew rotation, what was the gravity reading?:'))
            first_rtn_bbl = float(st.text_input('for the first brew rotation, what was the barrel count?:'))
            second_rtn_OG = float(st.text_input('for the second brew rotation, what was the gravity reading?:'))
            second_rtn_bbl = float(st.text_input('for the second brew rotation, what was the barrel count?:'))
            rotation_lists[0].append(first_rtn_OG)
            rotation_lists[0].append(first_rtn_bbl)
            rotation_lists[1].append(second_rtn_OG)
            rotation_lists[1].append(second_rtn_bbl)
        except ValueError:
            pass
        break
    elif len(rotation_lists) == 3:
        try:
            first_rtn_OG = float(st.text_input('for the first brew rotation, what was the gravity reading?:'))
            first_rtn_bbl = float(st.text_input('for the first brew rotation, what was the barrel count?:'))
            second_rtn_OG = float(st.text_input('for the second brew rotation, what was the gravity reading?:'))
            second_rtn_bbl = float(st.text_input('for the second brew rotation, what was the barrel count?:'))
            third_rtn_OG = float(st.text_input('for the third brew rotation, what was the gravity reading?:'))
            third_rtn_bbl = float(st.text_input('for the third brew rotation, what was the barrel count?:'))
            rotation_lists[0].append(first_rtn_OG)
            rotation_lists[0].append(first_rtn_bbl)
            rotation_lists[1].append(second_rtn_OG)
            rotation_lists[1].append(second_rtn_bbl)
            rotation_lists[2].append(third_rtn_OG)
            rotation_lists[2].append(third_rtn_bbl)
        except ValueError:
            pass
        break
    elif len(rotation_lists) == 4:
        try:
            first_rtn_OG = float(st.text_input('for the first brew rotation, what was the gravity reading?:'))
            first_rtn_bbl = float(st.text_input('for the first brew rotation, what was the barrel count?:'))
            second_rtn_OG = float(st.text_input('for the second brew rotation, what was the gravity reading?:'))
            second_rtn_bbl = float(st.text_input('for the second brew rotation, what was the barrel count?:'))
            third_rtn_OG = float(st.text_input('for the third brew rotation, what was the gravity reading?:'))
            third_rtn_bbl = float(st.text_input('for the third brew rotation, what was the barrel count?:'))
            fourth_rtn_OG = float(st.text_input('for the fourth brew rotation, what was the gravity reading?:'))
            fourth_rtn_bbl = float(st.text_input('for the fourth brew rotation, what was the barrel count?:'))
            rotation_lists[0].append(first_rtn_OG)
            rotation_lists[0].append(first_rtn_bbl)
            rotation_lists[1].append(second_rtn_OG)
            rotation_lists[1].append(second_rtn_bbl)
            rotation_lists[2].append(third_rtn_OG)
            rotation_lists[2].append(third_rtn_bbl)
            rotation_lists[3].append(fourth_rtn_OG)
            rotation_lists[3].append(fourth_rtn_bbl)
        except ValueError:
            pass
        break
    else:
        print('Looks like you fell outside the range of rotations, try inputting 1 through 4 rotations instead.')
        break

# calculate brew batch metrics based on length of rotation list
for x in rotation_lists:
    if len(rotation_lists) == 1:
        try:
            batch_mass_one = float(rotation_lists[0][0]) * (rotation_lists[0][1])
            total_batch_mass = float(batch_mass_one)
            total_bbl_count = float(rotation_lists[0][1])
        except IndexError:
            pass
        break
    elif len(rotation_lists) == 2:
        try:
            batch_mass_one = float((rotation_lists[0][0]) * (rotation_lists[0][1]))
            batch_mass_two = float((rotation_lists[1][0]) * (rotation_lists[1][1]))
            total_batch_mass = float((batch_mass_one) + (batch_mass_two))
            total_bbl_count = float((rotation_lists[0][1]) + (rotation_lists[1][1]))
        except IndexError:
            pass
        break
    elif len(rotation_lists) == 3:
        try:
            batch_mass_one = float((rotation_lists[0][0]) * (rotation_lists[0][1]))
            batch_mass_two = float((rotation_lists[1][0]) * (rotation_lists[1][1]))
            batch_mass_three = float((rotation_lists[2][0]) * (rotation_lists[2][1]))
            total_batch_mass = float((batch_mass_one) + (batch_mass_two) + (batch_mass_three))
            total_bbl_count = float((rotation_lists[0][1]) + (rotation_lists[1][1]) + (rotation_lists[2][1]))
        except IndexError:
            pass
        break
    elif len(rotation_lists) == 4:
        try:
            batch_mass_one = float((rotation_lists[0][0]) * (rotation_lists[0][1]))
            batch_mass_two = float((rotation_lists[1][0]) * (rotation_lists[1][1]))
            batch_mass_three = float((rotation_lists[2][0]) * (rotation_lists[2][1]))
            batch_mass_four = float((rotation_lists[3][0]) * (rotation_lists[3][1]))
            total_batch_mass = float((batch_mass_one) + (batch_mass_two) + (batch_mass_three) + (batch_mass_four))
            total_bbl_count = float((rotation_lists[0][1]) + (rotation_lists[1][1]) + (rotation_lists[2][1])
                                    + (rotation_lists[3][1]))
        except IndexError:
            pass
        break
try:
    total_batch_og = total_batch_mass / total_bbl_count
except TypeError:
    pass

try:
    target_bbl = total_batch_mass / target_og
except TypeError:
    pass

try:
    hot_liquor = target_bbl - total_bbl_count
except TypeError:
    pass

try:
    final_bbl = total_bbl_count + round(hot_liquor)
except TypeError:
    pass

try:
    final_og = total_batch_mass / final_bbl
except TypeError:
    pass
if total_batch_mass != ():
    st.write('Your total batch mass so far is:', round(total_batch_mass, 2))
    st.write('Your total barrel count so far is:', total_bbl_count, 'barrels')

try:
    st.write('The current brew has an average gravity reading of:', round(total_batch_og, 2))
except TypeError:
    pass

try:
    st.write('You need', round(hot_liquor, 2), 'barrels to hit your target gravity value, rounded that value is ',
             round(hot_liquor),
             'barrels')
except TypeError:
    pass
try:
    if hot_liquor > 0:
        st.write('Doing this will give you a final gravity reading of ', round(final_og, 2))
    elif hot_liquor < 0:
        st.write("since your hot liquor calculation is negative, you don\'t need to do anything!")
except TypeError:
    pass

if total_batch_mass != ():
    st.write('Good luck with your brew!')
