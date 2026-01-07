# Indexing
print("\nv\tpositive indexing ")
pos_index = "syed haji shah"
print(pos_index[3], pos_index[8], pos_index[13])  # d, i, h
ch = pos_index[0] + pos_index[5] + pos_index[10]  # s, h, s
print(ch)

# Negative Indexing
print("\nvi\tnegative indexing ")
neg_index = "syed haji shah"
print(neg_index[-1], neg_index[-6], neg_index[-12])  # h, i, s
ch2 = neg_index[-14] + neg_index[-9] + neg_index[-4]  # s, h, s
print(ch2)

# Slicing
print("\nvii\tslicing of string ")
slice_str = "syed haji shah"
print(len(slice_str))
print(slice_str[0:4])    # syed (0 to 3)
print(slice_str[5:])     # haji shah (5 to end)
print(slice_str[:])      # syed haji shah (entire string)
print(slice_str[0:14:2]) # 'se aisa' (indices 0,2,4,6,8,10,12 -> picks every 2nd char)
print(slice_str[::3])    # 'sda a' (whole string with step 3 -> indices 0,3,6,9,12)