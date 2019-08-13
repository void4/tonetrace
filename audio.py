import mido

print(mido.get_output_names())

output = mido.open_output("TiMidity:TiMidity port 0")#"Midi Through:Midi Through Port-0")

def on(f):
	output.send(mido.Message("note_on", note=f))#, velocity=50, channel=chan))

def off(f):
	output.send(mido.Message("note_off", note=f))
