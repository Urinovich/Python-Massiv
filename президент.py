Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> text="""
George Washington, 1789-1797
John Adams, 1797-1801
Thomas Jefferson, 1801-1809
James Madison, 1809-1817
James Monroe, 1817-1825
John Quincy Adams, 1825-1829
Andrew Jackson, 1829-1837
Martin Van Buren, 1837-1841
William Henry Harrison, 1841
John Tyler, 1841-1845
James Knox Polk, 1845-1849
Zachary Taylor, 1849-1850
Millard Fillmore, 1850-1853
Franklin Pierce, 1853-1857
James Buchanan, 1857-1861
Abraham Lincoln, 1861-1865
Andrew Johnson, 1865-1869
Ulysses S. Grant, 1869-1877
Rutherford Birchard Hayes, 1877-1881
James Abram Garfield, 1881
Chester Alan Arthur, 1881-1885
Grover Cleveland, 1885-1889
Benjamin Harrison, 1889-1893
Grover Cleveland, 1893-1897
William McKinley, 1897-1901
Theodore Roosevelt, 1901-1909
William Howard Taft, 1909-1913
Woodrow Wilson, 1913-1921
Warren Gamaliel Harding, 1921-1923
Calvin Coolidge, 1923-1929
Herbert Clark Hoover, 1929-1933
Franklin Delano Roosevelt, 1933-1945
Harry S. Truman, 1945-1953
Dwight David Eisenhower, 1953-1961
John Fitzgerald Kennedy, 1961-1963
Lyndon Baines Johnson, 1963-1969
Richard Milhous Nixon, 1969-1974
Gerald Rudolph Ford, 1974-1977
James Earl Carter, Jr., 1977-1981
Ronald Wilson Reagan, 1981-1989
George Herbert Walker Bush, 1989-1993
William Jefferson Clinton, 1993-2001
George Walker Bush, 2001-2009
Barack Hussein Obama, 2009-
"""
>>> for name, start, end in re.findall(r'(\D+)(\d+)-(\d+)', text):
	print('{}, {} years'.format(name, int(end) - int(start)))

	

George Washington, , 8 years

John Adams, , 4 years

Thomas Jefferson, , 8 years

James Madison, , 8 years

James Monroe, , 8 years

John Quincy Adams, , 4 years

Andrew Jackson, , 8 years

Martin Van Buren, , 4 years

John Tyler, , 4 years

James Knox Polk, , 4 years

Zachary Taylor, , 1 years

Millard Fillmore, , 3 years

Franklin Pierce, , 4 years

James Buchanan, , 4 years

Abraham Lincoln, , 4 years

Andrew Johnson, , 4 years

Ulysses S. Grant, , 8 years

Rutherford Birchard Hayes, , 4 years

Chester Alan Arthur, , 4 years

Grover Cleveland, , 4 years

Benjamin Harrison, , 4 years

Grover Cleveland, , 4 years

William McKinley, , 4 years

Theodore Roosevelt, , 8 years

William Howard Taft, , 4 years

Woodrow Wilson, , 8 years

Warren Gamaliel Harding, , 2 years

Calvin Coolidge, , 6 years

Herbert Clark Hoover, , 4 years

Franklin Delano Roosevelt, , 12 years

Harry S. Truman, , 8 years

Dwight David Eisenhower, , 8 years

John Fitzgerald Kennedy, , 2 years

Lyndon Baines Johnson, , 6 years

Richard Milhous Nixon, , 5 years

Gerald Rudolph Ford, , 3 years

James Earl Carter, Jr., , 4 years

Ronald Wilson Reagan, , 8 years

George Herbert Walker Bush, , 4 years

William Jefferson Clinton, , 8 years

George Walker Bush, , 8 years
>>> 
