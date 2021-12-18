echo "Installing Packages ... "
pkg install git clone
clear
echo "Installing Tool ... "
git clone  https://github.com/mf4TN/Combo-Dumper.py.git
clear
echo "installing Python ..."
pkg install python
clear
echo "Done Installed All Packages "
echo "Running Tool ..."
mv Combo-Dumper.py combo_maker
cd combo_maker 
clear
echo "running..."
python 'Combo Dumper.py'
