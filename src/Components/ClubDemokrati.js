import SongCover from './SongCover.js'
import React from 'react';
import './ClubDemokrati.css';

class ClubDemokrati extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            voted: false,
            nowPlaying: {
                id: 0,
                name: '',
                artist: '',
                votes: 0
            },
            songs: [
                {
                    id: 1,
                    name: 'Song 1',
                    artist: 'Artist 1',
                    votes: 0,
                    image: 'data:image/png;base64,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'
                },
                {
                    id: 2,
                    name: 'Song 2',
                    artist: 'Artist 2',
                    votes: 0,
                    image: 'data:image/png;base64,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'
                },
                {
                    id: 3,
                    name: 'Song 3',
                    artist: 'Artist 3',
                    votes: 0,
                    image: 'data:image/png;base64,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'
                },
                {
                    id: 4,
                    name: 'Song 4',
                    artist: 'Artist 4',
                    votes: 0,
                    image: 'data:image/png;base64,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'
                }
            ]
            
        }
    }

    getVote = (songId) => {
        if(!this.state.voted) {
            let newState = this.state;
            newState.voted = false;
            //Find song with the matching id and increment the votes
            newState.songs.forEach(song => {
                if(song.id === songId) {
                    song.votes++;
                }
            });
            this.setState(newState);
        }
    }

    render() {
        const songs = this.state.songs;
        return (
        <div className="ClubDemokrati">
            <h1>Now Playing</h1>
            <SongCover songName={this.state.nowPlaying.name} artist={this.state.nowPlaying.artist} votes={this.state.nowPlaying.votes}/>
            <div className="SongGrid">
                {songs.map((song) =>
                    <SongCover key={song.id} songId={song.id} songName={song.name} artist={song.artist} votes={song.votes} image={song.image} onVote={this.getVote.bind(this)} />
                )}
            </div>
        </div>
        );
    }
}

export default ClubDemokrati;