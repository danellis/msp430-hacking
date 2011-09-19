OBJECTS=lcd.o
TARGET=lcd.elf

%.o: %.c
	msp430-gcc -Werror -std=gnu99 -mmcu=msp430f5529 -c -o $@ $<

led.elf: $(OBJECTS)
	msp430-gcc -mmcu=msp430f5529 -o $(TARGET) $(OBJECTS)

deploy: $(TARGET)
	mspdebug rf2500 "prog $(TARGET)"

clean::
	rm -f $(TARGET) $(OBJECTS)
