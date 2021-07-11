echo " installing ... "
echo " package Git installing ..."
pkg install git 
pkg install clone
clear
echo " Git Installed ..."
git clone  https://github.com/mf4TN/Combo-Dumper.py.git
clear
echo " installing Python ..."
pkg install python
clear
echo " Done Install Packages "
echo " Running Tool ..."
mv Combo-Dumper.py combo_maker
cd combo_maker 
clear
echo "running..."
python 'Combo Dumper.py'
