import streamlit as st

st.title('Liquor Back Calculator')

target_og = st.text_input("Enter your target gravity value (e.g, 12.0):")
if target_og:
    target_og = float(target_og)
    rotation_count = st.text_input('How many rotations in this brew (1-4)?:')
if rotation_count:
    rotation_count = int(rotation_count)
rotation_lists = [[] for i in range(rotation_count)]

for x in rotation_lists:
    if len(rotation_lists) == 1:
        first_rtn_OG = float(st.text_input('for the first brew rotation, what was the OG value?:'))
        first_rtn_bbl = float(st.text_input('for the first brew rotation, what was the barrel count?:'))
        rotation_lists[0].append(first_rtn_OG)
        rotation_lists[0].append(first_rtn_bbl)
        break
    elif len(rotation_lists) == 2:
        first_rtn_OG = float(st.text_input('for the first brew rotation, what was the OG value?:'))
        first_rtn_bbl = float(st.text_input('for the first brew rotation, what was the barrel count?:'))
        second_rtn_OG = float(st.text_input('for the second brew rotation, what was the OG value?:'))
        second_rtn_bbl = float(st.text_input('for the second brew rotation, what was the barrel count?:'))
        rotation_lists[0].append(first_rtn_OG)
        rotation_lists[0].append(first_rtn_bbl)
        rotation_lists[1].append(second_rtn_OG)
        rotation_lists[1].append(second_rtn_bbl)
        break
    elif len(rotation_lists) == 3:
        first_rtn_OG = float(st.text_input('for the first brew rotation, what was the OG value?:'))
        first_rtn_bbl = float(st.text_input('for the first brew rotation, what was the barrel count?:'))
        second_rtn_OG = float(st.text_input('for the second brew rotation, what was the OG value?:'))
        second_rtn_bbl = float(st.text_input('for the second brew rotation, what was the barrel count?:'))
        third_rtn_OG = float(st.text_input('for the third brew rotation, what was the OG value?:'))
        third_rtn_bbl = float(st.text_input('for the third brew rotation, what was the barrel count?:'))
        rotation_lists[0].append(first_rtn_OG)
        rotation_lists[0].append(first_rtn_bbl)
        rotation_lists[1].append(second_rtn_OG)
        rotation_lists[1].append(second_rtn_bbl)
        rotation_lists[2].append(third_rtn_OG)
        rotation_lists[2].append(third_rtn_bbl)
        break
    elif len(rotation_lists) == 4:
        first_rtn_OG = float(st.text_input('for the first brew rotation, what was the OG value?:'))
        first_rtn_bbl = float(st.text_input('for the first brew rotation, what was the barrel count?:'))
        second_rtn_OG = float(st.text_input('for the second brew rotation, what was the OG value?:'))
        second_rtn_bbl = float(st.text_input('for the second brew rotation, what was the barrel count?:'))
        third_rtn_OG = float(st.text_input('for the third brew rotation, what was the OG value?:'))
        third_rtn_bbl = float(st.text_input('for the third brew rotation, what was the barrel count?:'))
        fourth_rtn_OG = float(st.text_input('for the fourth brew rotation, what was the OG value?:'))
        fourth_rtn_bbl = float(st.text_input('for the fourth brew rotation, what was the barrel count?:'))
        rotation_lists[0].append(first_rtn_OG)
        rotation_lists[0].append(first_rtn_bbl)
        rotation_lists[1].append(second_rtn_OG)
        rotation_lists[1].append(second_rtn_bbl)
        rotation_lists[2].append(third_rtn_OG)
        rotation_lists[2].append(third_rtn_bbl)
        rotation_lists[3].append(fourth_rtn_OG)
        rotation_lists[3].append(fourth_rtn_bbl)
        break
    else:
        print('Looks like you fell outside the range of rotations, try inputting 1 through 4 rotations instead.')
        break

for x in rotation_lists:
    if len(rotation_lists) == 1:
        batch_mass_one = float(rotation_lists[0][0]) * (rotation_lists[0][1])
        total_batch_mass = float(batch_mass_one)
        total_bbl_count = float(rotation_lists[0][1])
        break
    elif len(rotation_lists) == 2:
        batch_mass_one = float((rotation_lists[0][0]) * (rotation_lists[0][1]))
        batch_mass_two = float((rotation_lists[1][0]) * (rotation_lists[1][1]))
        total_batch_mass = float((batch_mass_one) + (batch_mass_two))
        total_bbl_count = float((rotation_lists[0][1]) + (rotation_lists[1][1]))
        break
    elif len(rotation_lists) == 3:
        batch_mass_one = float((rotation_lists[0][0]) * (rotation_lists[0][1]))
        batch_mass_two = float((rotation_lists[1][0]) * (rotation_lists[1][1]))
        batch_mass_three = float((rotation_lists[2][0]) * (rotation_lists[2][1]))
        total_batch_mass = float((batch_mass_one) + (batch_mass_two) + (batch_mass_three))
        total_bbl_count = float((rotation_lists[0][1]) + (rotation_lists[1][1]) + (rotation_lists[2][1]))
        break
    elif len(rotation_lists) == 4:
        batch_mass_one = float((rotation_lists[0][0]) * (rotation_lists[0][1]))
        batch_mass_two = float((rotation_lists[1][0]) * (rotation_lists[1][1]))
        batch_mass_three = float((rotation_lists[2][0]) * (rotation_lists[2][1]))
        batch_mass_four = float((rotation_lists[3][0]) * (rotation_lists[3][1]))
        total_batch_mass = float((batch_mass_one) + (batch_mass_two) + (batch_mass_three) + (batch_mass_four))
        total_bbl_count = float((rotation_lists[0][1]) + (rotation_lists[1][1]) + (rotation_lists[2][1])
                                + (rotation_lists[3][1]))
        break

total_batch_og = total_batch_mass / total_bbl_count
target_bbl = total_batch_mass / target_og
hot_liquor = target_bbl - total_bbl_count
final_bbl = total_bbl_count + round(hot_liquor)
final_og = total_batch_mass / final_bbl

print('Your total batch mass is {:0.2f}'.format(total_batch_mass))
st.write('Your total batch mass so far is:', total_batch_mass)
print('Your total barrel count is {:0.2f}'.format(total_bbl_count))
st.write('Your total barrel count so far is:', total_bbl_count)
print('The current brew has an average gravity reading of {:0.2f}'.format(total_batch_og))
st.write('The current brew has an average gravity reading of:', round(total_batch_og, 4))
print('You need {:0.2f} barrels to hit your target OG, rounded that value is {} barrels'.format(hot_liquor,
                                                                                                round(hot_liquor)))
st.write('You need', round(hot_liquor, 2), 'barrels to hit your target OG, rounded that value is ', round(hot_liquor),
         'barrels')
if hot_liquor > 0:
    print('Doing this will give you a final og of {:0.2f}'.format(final_og))
    st.write('Doing this will give you a final gravity reading of ', round(final_og, 2))
elif hot_liquor < 0:
    st.write("since your hot liquor calculation is negative, you don\'t need to do anything!")
print('Good luck!')
st.text('Good Luck :)!')
