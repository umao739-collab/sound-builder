import json,subprocess,re,base64,sys
M=json.load(open('marks.json'));bank={}
for src,d in M.items():
    for id,(a,b) in d.items():
        if id in('tch','ss','ll','ear','air'):continue
        dur=b-a;pad=0.04;a0=max(0,a-pad);dur+=pad*2
        base=['ffmpeg','-y','-v','error','-ss',str(a0),'-t',str(dur),'-i',f'src/{src}.mp3','-ac','1']
        o=subprocess.run([x for x in base if x not in('error','-v')]+['-af','volumedetect','-f','null','-'],capture_output=True,text=True).stderr
        mx=float(re.search(r'max_volume: (-?[\d.]+)',o).group(1));g=-2.0-mx
        fo=max(0,dur-0.03)
        out=f'clips/{id}.mp3'
        subprocess.run(base+['-af',f'volume={g}dB,afade=t=in:d=0.012,afade=t=out:st={fo}:d=0.03','-ar','44100','-b:a','64k',out],check=True)
        bank[id]='data:audio/mpeg;base64,'+base64.b64encode(open(out,'rb').read()).decode()
json.dump(bank,open('bank.json','w'))
s=open('app/sound-builder.html').read()
j=json.dumps(bank,separators=(',',':'))
s=re.sub(r'/\*SOUND_BANK_START\*/.*?/\*SOUND_BANK_END\*/','/*SOUND_BANK_START*/'+j.replace('\\','\\\\')+'/*SOUND_BANK_END*/',s,flags=re.S)
open('app/sound-builder-full.html','w').write(s)
print(len(bank),len(s)//1024,'KB',sorted(bank))
