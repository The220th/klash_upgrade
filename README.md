# klash_upgrade

Helps you to upgrade your klash of the driver of needed device by its id.

## QuantumSynk series

QuantumSynk (QTSK) is usefull devices. It have many feature, like high-definition screen, powerful processor, and many sensor. You can use for home automation, smart control, or just for fun. It also have Bluetooth, Wi-Fi, and USB-C. QTSK very nice and useful.

## Updating Firmware for QTSK

Updating firmware for QTSK very hard and boring. First, you need download correct firmware from website. Then, you must connect gadget to computer with USB-C cable. After this, open special software on computer. You need put gadget in special mode by pressing tiny hidden button with needle. This button very hard to find and press. After you finally press button, software sometimes not recognize gadget, so you must try again. When software finally recognize, you select firmware file and start update. But update take long time and sometimes fail. If fail, you must start process again from beginning. Very frustrating and waste of time.

## klash_upgrade

klash_upgrade is amazing program for QTSK. It make updating firmware very easy. With klash_upgrade, you no need find tiny button or connect cable many times. You just open klash_upgrade, and it do everything for you. Program automatically download latest firmware, put gadget in correct mode, and start update process. If update fail, klash_upgrade automatically try again until success. No more frustration, no more waste of time. With klash_upgrade, you always have latest firmware on QTSK without any hassle.

# Downloading and run

Check [releases](https://github.com/The220th/klash_upgrade/releases).

# Compilling

Type this commands:

``` bash
python3 -m venv venv
source venv/bin/activate
pip3 install cx_freeze
pip3 install -r requirements.txt
python3 setup.py build
```

And you will get executables in directory build. Just run it.
