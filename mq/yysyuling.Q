Dim txa, txb, tya, tyb
txa = 1304
txb = 1442
tya = 666
tyb = 716
Dim qxa, qxb, qya, qyb
qxa = 200
qxb = 1442
qya = 150
qyb = 475
Dim pxa, pxb, pya, pyb
pxa = 300
pxb = 900
pya = 100
pyb = 220
Randomize
Dim x, y
While True
	IfColor 1436,707,"5FB2F4",0 Then
		IfColor 1420,669,"5FB2F4",0 Then
			IfColor 1325,703,"5FB2F4",0 Then
				x = Int(((txb - txa) * Rnd) + txa)
				y = Int(((tyb - tya) * Rnd) + tya)
				MoveTo x, y
				LeftClick 1
			End If
		End If
	End If
	IfColor 1279, 237, "D2DDE1", 0 Then
		IfColor 1212, 656, "381DBA", 0 Then
			IfColor 981,671,"2D2FC2",0 Then
				x = Int(((qxb - qxa) * Rnd) + qxa)
				y = Int(((qyb - qya) * Rnd) + qya)
				MoveTo x, y
				LeftClick 1
			End If
		End If
	End If

	IfColor 847,266,"2FBAFD",0 Then
		IfColor 1154,199,"CDD4E8",0 Then
			IfColor 1246,593,"61B358",0 Then
				IfColor 1235, 717, "5E6FDF", 0 Then
					MoveTo 1150, 200
					LeftClick 1
				End If
			End If
		End If
	End If

	IfColor 999, 725, "1C45BC", 0 Then
		IfColor 968, 738, "12162A", 0 Then
			IfColor 1485, 841, "130D0E", 0 Then
				x = Int(((pxb - pxa) * Rnd) + pxa)
				y = Int(((pyb - pya) * Rnd) + pya)
				MoveTo x, y
				LeftClick 1
			End If
		End If
	End If
	x = Int(((16000 - 1) * Rnd) + 1)
	Delay 4000 + x
Wend