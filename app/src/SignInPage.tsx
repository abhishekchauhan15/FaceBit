import React, { useState, useRef, useCallback } from 'react'
import Webcam from 'react-webcam'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"

export default function SignInPage() {
  const [capturedImage, setCapturedImage] = useState<string | null>(null)
  const webcamRef = useRef<Webcam>(null)

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current?.getScreenshot()
    if (imageSrc) {
      setCapturedImage(imageSrc)
    }
  }, [webcamRef])

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    // Handle form submission here
  }

  return (
    <main className="flex items-center justify-center min-h-screen bg-background">
      <Card className="w-full max-w-[650px]">
        <CardHeader>
          <CardTitle className="text-center">Sign in to our platform</CardTitle>
        </CardHeader>
        <CardContent>
          <img src="/secure_login.png" alt="Secure Login" className="w-full mb-4" />
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="email">Email</Label>
              <Input id="email" name="email" type="email" placeholder="example@company.com" required />
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input id="password" name="password" type="password" placeholder="Password" required />
            </div>
            <div className="space-y-2">
              <Label htmlFor="user_type">Choose User Type</Label>
              <Select name="user_type" required>
                <SelectTrigger>
                  <SelectValue placeholder="Select user type" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="student">Student</SelectItem>
                  <SelectItem value="teacher">Professor</SelectItem>
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label>Capture Image</Label>
              <div className="space-y-2">
                <Webcam
                  audio={false}
                  ref={webcamRef}
                  screenshotFormat="image/jpeg"
                  videoConstraints={{ width: 370, height: 320 }}
                  className="w-full max-w-[370px] h-[320px]"
                />
                <Button type="button" onClick={capture}>Capture Image</Button>
              </div>
              {capturedImage && (
                <div>
                  <img src={capturedImage} alt="Captured" className="w-full max-w-[370px] h-[320px]" />
                </div>
              )}
              <input type="hidden" name="image_hidden" value={capturedImage || ''} />
            </div>
            <div className="flex justify-between items-center">
              <a href="/lostpassword" className="text-primary hover:underline">Lost password?</a>
            </div>
            <Button type="submit" className="w-full">Sign in</Button>
          </form>
          <div className="mt-4 text-center">
            <span>
              Not registered?{' '}
              <a href="/register" className="text-primary hover:underline">Create account</a>
            </span>
          </div>
        </CardContent>
      </Card>
    </main>
  )
}